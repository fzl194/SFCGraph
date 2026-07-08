---
id: UDG@20.15.2@MMLCommand@DSP TUNNELINFO
type: MMLCommand
name: DSP TUNNELINFO（显示隧道信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TUNNELINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道信息
status: active
---

# DSP TUNNELINFO（显示隧道信息）

## 功能

该命令用于显示本设备上建立成功的隧道的基本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TUNNELID | 隧道ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～20。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TUNNELINFO]] · 隧道信息（TUNNELINFO）

## 使用实例

显示指定的TUNNEL：

```
DSP TUNNELINFO: TUNNELID="0x000000000300000001";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
        隧道ID =  0x000000000300000001
      隧道类型 =  Gre
      隧道目的 =  10.1.1.1
      隧道状态 =  Down
      隧道Cost =  0
      隧道名字 =  Tunnel1
隧道出接口名字 =  Ethernet65/0/3.101
    隧道下一跳 =  10.1.1.0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TUNNELINFO.md`
