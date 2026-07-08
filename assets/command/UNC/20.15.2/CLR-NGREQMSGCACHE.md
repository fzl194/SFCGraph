---
id: UNC@20.15.2@MMLCommand@CLR NGREQMSGCACHE
type: MMLCommand
name: CLR NGREQMSGCACHE（清空DNS客户端的缓存消息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGREQMSGCACHE
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# CLR NGREQMSGCACHE（清空DNS客户端的缓存消息）

## 功能

**适用NF：AMF**

该命令用于清空请求消息缓存链中所有缓存消息。

AMF可向系统的DNS客户端微服务查询MME，当DNS客户端相关配置命令正确，但一直查询不到MME的IP，执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行后，消息缓存链中的请求消息会丢失，不会给AMF响应。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGREQMSGCACHE]] · 清空DNS客户端的缓存消息（NGREQMSGCACHE）

## 使用实例

清空请求消息缓存链中所有缓存消息：

```
CLR NGREQMSGCACHE:
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清空DNS客户端的缓存消息（CLR-NGREQMSGCACHE）_17555436.md`
