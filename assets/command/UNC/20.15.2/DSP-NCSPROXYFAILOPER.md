---
id: UNC@20.15.2@MMLCommand@DSP NCSPROXYFAILOPER
type: MMLCommand
name: DSP NCSPROXYFAILOPER（显示NETCONF代理操作失败信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSPROXYFAILOPER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSPROXYFAILOPER（显示NETCONF代理操作失败信息）

## 功能

该命令用于NETCONF代理操作失败信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCSPROXYFAILOPER]] · NETCONF代理操作失败信息（NCSPROXYFAILOPER）

## 使用实例

NETCONF代理操作失败信息：

```
DSP NCSPROXYFAILOPER:;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
NETCONF会话ID  =  316
       时间戳  =  2017-10-11, 00:31:09:737
    NLS通道ID  =  5
      NLS名称  =  kk
     错误信息  =  系统正忙，请稍后重试。;MessageId=82
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSPROXYFAILOPER.md`
