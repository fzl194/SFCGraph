---
id: UNC@20.15.2@MMLCommand@DSP LSPVSTATISTICS
type: MMLCommand
name: DSP LSPVSTATISTICS（显示LSPV报文统计计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LSPVSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 系统维护
- Ping和Tracert
- LSPV
status: active
---

# DSP LSPVSTATISTICS（显示LSPV报文统计计数）

## 功能

该命令用于显示LSPV报文统计计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LSPVSTATISTICS]] · LSPV报文统计计数（LSPVSTATISTICS）

## 使用实例

显示LSPV报文统计计数：

```
DSP LSPVSTATISTICS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                    发包总数  = 0
                    收包总数  = 0
            发送请求报文总数  = 0
            接收请求报文总数  = 0
            发送应答报文总数  = 0
            接收应答报文总数  = 0
接口下协议去使能丢弃报文总数  = 0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示LSPV报文统计计数（DSP-LSPVSTATISTICS）_50121658.md`
