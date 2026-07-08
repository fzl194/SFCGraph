---
id: UNC@20.15.2@MMLCommand@DSP SRIIDINFO
type: MMLCommand
name: DSP SRIIDINFO（显示静态路由IID信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SRIIDINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 静态路由调测
status: active
---

# DSP SRIIDINFO（显示静态路由IID信息）

## 功能

该命令用于显示本设备上静态路由使用的IID信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IPv4静态路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| INDIRECTID | 直连IID | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态路由IID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [静态路由IID信息（SRIIDINFO）](configobject/UNC/20.15.2/SRIIDINFO.md)

## 使用实例

显示本设备上静态路由使用的IID信息：

```
DSP SRIIDINFO:AFTYPE=ipv4unicast, INDIRECTID="1d00005d";
```

```

RETCODE = 0  操作成功.

结果如下
------------------------
             直连IID  =  0x1d00005d
                VPID  =  0
            源下一跳  =  10.1.1.0
        配置接口名字  =  Ethernet64/0/3
             VPN名字  =  _public_
       下一跳所在VPN  =  NULL
          前缀所在表  =  base
                标记  =  DG
            参考计数  =  1
            迭代类型  =  NO Relay
            迭代深度  =  0
   上一次分配IID时间  =  2016-03-22 09:49:12
   上一次回收IID时间  =  NULL
      上一次Up的时间  =  2016-03-22 09:49:12
    上一次Down的时间  =  NULL
            本机地址  =  10.1.1.1
            远端地址  =  0.0.0.0
            接口状态  =  UP
          迭代下一跳  =  0.0.0.0
            接口名字  =  NULL
              隧道ID  =  NULL
            抑制计数  =  0
    抑制剩余时间（s） =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示静态路由IID信息（DSP-SRIIDINFO）_00866741.md`
