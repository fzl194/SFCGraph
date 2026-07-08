---
id: UDG@20.15.2@MMLCommand@DSP RULEMATCHPARA
type: MMLCommand
name: DSP RULEMATCHPARA（显示规则匹配报文信息构造状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RULEMATCHPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则匹配测试
- 规则匹配报文参数
status: active
---

# DSP RULEMATCHPARA（显示规则匹配报文信息构造状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示规则匹配报文信息构造状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PACKETSOURCE | 报文信息来源 | 可选必选说明：可选参数<br>参数含义：规则匹配时选择的报文信息来源。<br>数据来源：本端规划<br>取值范围：<br>- USER_DEFINED：表示选择规则匹配时使用的报文信息为自定义。<br>默认值：无<br>配置原则：指定报文信息来源。 |

## 操作的配置对象

- [规则匹配报文信息构造状态（RULEMATCHPARA）](configobject/UDG/20.15.2/RULEMATCHPARA.md)

## 使用实例

显示规则匹配报文信息构造状态：

```
DSP RULEMATCHPARA: PACKETSOURCE=USER_DEFINED;
```

```

RETCODE = 0  Operation succeeded

The Status Of Packet Information Construction Required For Rule Matching
------------------------------------------------------------------------
                       Source of The Packet Information  =  user defined
Status Of Rule Matching Packet Information Construction  =  done
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示规则匹配报文信息构造状态（DSP-RULEMATCHPARA）_89650065.md`
