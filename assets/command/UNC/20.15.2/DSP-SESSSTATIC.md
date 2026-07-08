---
id: UNC@20.15.2@MMLCommand@DSP SESSSTATIC
type: MMLCommand
name: DSP SESSSTATIC（显示会话消息统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SESSSTATIC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 对端消息统计
status: active
---

# DSP SESSSTATIC（显示会话消息统计信息）

## 功能

该命令用于显示Diameter会话消息统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SESSSTATIC]] · 会话消息统计信息（SESSSTATIC）

## 使用实例

显示Diameter会话消息统计信息：

```
DSP SESSSTATIC:;
```

```

RETCODE = 0 操作成功

结果如下
-------------------------
            对端地址  =  10.1.1.100
        发送对端消息  =  33
        接收对端消息  =  34
        丢弃用户消息  =  1
        最大延迟时间  =  1
  发送失败的消息计数  =  0
接收到的错误报文计数  =  0
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示会话消息统计信息（DSP-SESSSTATIC）_00865601.md`
