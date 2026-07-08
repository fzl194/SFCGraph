---
id: UDG@20.15.2@MMLCommand@DSP SRIPV6IIDINFO
type: MMLCommand
name: DSP SRIPV6IIDINFO（显示IPv6静态路由IID信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRIPV6IIDINFO
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

# DSP SRIPV6IIDINFO（显示IPv6静态路由IID信息）

## 功能

该命令用于显示本设备上IPv6静态路由使用的IID信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IPv6静态路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| INDIRECTID | 直连IID | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态路由IID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRIPV6IIDINFO]] · IPv6静态路由IID信息（SRIPV6IIDINFO）

## 使用实例

显示本设备上IPv6静态路由使用的IID信息：

```
DSP SRIPV6IIDINFO:AFTYPE=ipv6unicast,INDIRECTID="E6000071";
```

```

RETCODE = 0  操作成功.

结果如下
------------------------
             直连IID  =  0xe6000071
                VPID  =  1
            源下一跳  =  2001:db8::1
        配置接口名字  =  NULL
             VPN名字  =  _public_
       下一跳所在VPN  =  _public_
          前缀所在表  =  base
                标记  =  DG
            参考计数  =  1
            迭代类型  =  IP Relay
            迭代深度  =  1
   上一次分配IID时间  =  2016-03-25 03:54:21
   上一次回收IID时间  =  NULL
      上一次Up的时间  =  2016-03-25 03:54:21
    上一次Down的时间  =  NULL
            本机地址  =  ::
            远端地址  =  ::
            接口状态  =  NULL
          迭代下一跳  =  2001:db8::2
            接口名字  =  LoopBack1
              隧道ID  =  NULL
            抑制计数  =  0
    抑制剩余时间（s） =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPv6静态路由IID信息（DSP-SRIPV6IIDINFO）_50121798.md`
