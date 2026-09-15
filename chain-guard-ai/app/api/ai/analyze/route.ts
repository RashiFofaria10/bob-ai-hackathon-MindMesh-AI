import { NextRequest, NextResponse } from "next/server"

const AI_API_URL = "http://127.0.0.1:8000/analyze"

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()

    const response = await fetch(AI_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    })

    const data = await response.json()

    if (!response.ok) {
      return NextResponse.json(
        {
          success: false,
          error: data.error || "AI service failed",
        },
        { status: response.status }
      )
    }

    return NextResponse.json(data)
  } catch (error) {
    console.error("AI API error:", error)

    return NextResponse.json(
      {
        success: false,
        error: "Could not connect to ChainGuard AI service",
        details:
          error instanceof Error
            ? error.message
            : "Unknown error",
      },
      { status: 500 }
    )
  }
}