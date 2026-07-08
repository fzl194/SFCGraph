---
id: UDG@20.15.2@MMLCommand@SET CFCACHEPARA
type: MMLCommand
name: SET CFCACHEPARA（设置内容过滤缓存参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CFCACHEPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤缓存参数配置
status: active
---

# SET CFCACHEPARA（设置内容过滤缓存参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置内容过滤缓存相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 开启内容过滤缓存会导致URL过滤策略不能及时更新，具体更新周期取决于本命令和ICAP Server上的缓存过期时间。
- CACHEIDLETIME参数配置值小于60秒时，系统实际按照60s进行缓存超时处理。修改CACHEIDLETIME参数前请评估对业务的影响，如果配置过小，会导致缓存策略更新过于频繁，影响性能；如果配置过大，会导致缓存策略更新不及时。如果无法评估请联系华为技术支持。
- 不建议修改参数CACHEIDLETIME，误配后缓冲时间过程，实际能力和配置不匹配。执行命令前请评估对业务的影响，如果无法评估请联系华为技术支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CACHEIDLETIME | CACHESW |
| --- | --- | --- |
| 初始值 | 300 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CACHEIDLETIME | 本地缓存过期时间 | 可选必选说明：可选参数<br>参数含义：该参数用于设置本地缓存过期时间。<br>数据来源：全网规划<br>取值范围：0-4294967294，单位是秒<br>默认值：无<br>配置原则：无 |
| CACHESW | 缓存开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤本地缓存功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFCACHEPARA]] · 内容过滤缓存参数（CFCACHEPARA）

## 关联任务

- [[UDG@20.15.2@Task@0-00258]]

## 使用实例

配置本地缓存过期时间为3600，设置本地缓存开关为开启：

```
SET CFCACHEPARA: CACHEIDLETIME=3600, CACHESW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CFCACHEPARA.md`
