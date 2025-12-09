from __future__ import annotations
import asyncio
import logging
from decimal import Decimal
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any

import httpx
from pydantic import BaseSettings, AnyHttpUrl, Field, validator
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy import (
    Column, Integer, String, DateTime, Numeric, select, desc
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import declarative_base, sessionmaker
