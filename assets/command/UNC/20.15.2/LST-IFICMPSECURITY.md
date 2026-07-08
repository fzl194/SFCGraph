---
id: UNC@20.15.2@MMLCommand@LST IFICMPSECURITY
type: MMLCommand
name: LST IFICMPSECURITY（查询接口下ICMP安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFICMPSECURITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- 接口下ICMP安全配置
status: active
---

# LST IFICMPSECURITY（查询接口下ICMP安全配置）

## 功能

该命令用于查询接口下ICMP安全配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数表示ICMP安全配置生效的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFICMPSECURITY]] · 接口下ICMP安全配置（IFICMPSECURITY）

## 使用实例

查询接口Ethernet64/0/3上发送报文能力的ICMP安全配置实例：

```
LST IFICMPSECURITY:IFNAME="Ethernet64/0/3";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
              接口名  =  Ethernet64/0/3
            报文方向  =  接收报文
        ICMP配置类型  =  报文类型
        ICMP报文类型  =  回显请求：Type=8, Code=0
                类型  =  8
                编码  =  0
        ICMP配置开关  =  使能
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IFICMPSECURITY.md`
