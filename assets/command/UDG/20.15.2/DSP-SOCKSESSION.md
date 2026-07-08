---
id: UDG@20.15.2@MMLCommand@DSP SOCKSESSION
type: MMLCommand
name: DSP SOCKSESSION（查询SOCK会话诊断信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SOCKSESSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SOCKET
status: active
---

# DSP SOCKSESSION（查询SOCK会话诊断信息）

## 功能

该命令用于查询SOCK会话诊断信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPCID | APP组件CID | 可选必选说明：必选参数<br>参数含义：该参数用来指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SOCKID | Socket实例ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [SOCK会话诊断信息（SOCKSESSION）](configobject/UDG/20.15.2/SOCKSESSION.md)

## 使用实例

查询SOCK会话诊断信息：

```
DSP SOCKSESSION: APPCID="0x8069003D",SOCKID=3;
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
            会话类型  =  7
             VPN索引  =  4294967295
        本地IPv4地址  =  0.0.0.0
        本地IPv6地址  =  ::
        对端IPv4地址  =  0.0.0.0
        对端IPv6地址  =  ::
          本地端口号  =  0
          对端端口号  =  0
          IPID起始值  =  0
          IPID结束值  =  0
           最小TTL值  =  0
           最大TTL值  =  0
              协议号  =  35074
            接口索引  =  0
             MAC地址  =  0000-0000-0000
                域ID  =  5
        应用层协议号  =  30
              序列号  =  2
            私有标志  =  0
            标志偏移  =  0
            标志长度  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SOCK会话诊断信息（DSP-SOCKSESSION）_49802494.md`
