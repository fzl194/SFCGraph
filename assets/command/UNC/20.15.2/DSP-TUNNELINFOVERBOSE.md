---
id: UNC@20.15.2@MMLCommand@DSP TUNNELINFOVERBOSE
type: MMLCommand
name: DSP TUNNELINFOVERBOSE（显示隧道详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TUNNELINFOVERBOSE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道详细信息
status: active
---

# DSP TUNNELINFOVERBOSE（显示隧道详细信息）

## 功能

该命令用于显示本设备上建立成功的隧道的详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TUNNELID | 隧道ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～20。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TUNNELINFOVERBOSE]] · 隧道详细信息（TUNNELINFOVERBOSE）

## 使用实例

显示建立成功的隧道的详细信息：

```
DSP TUNNELINFOVERBOSE:TUNNELID="0x000000000500000014";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
         隧道ID  =  0x000000000500000014
       隧道类型  =  Gre
   隧道目的地址  =  10.1.1.2
       隧道状态  =  Up
     隧道开销值  =  0
       隧道名字  =  Tunnel1
     使用类型名  =  Default
   最大传输单元  =  0
           深度  =  0
       更新时间  =  2016-03-22 11:04:21
    隧道所在VPN  =  _public_
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TUNNELINFOVERBOSE.md`
