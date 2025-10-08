package com.youngermaster.myapplication

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform