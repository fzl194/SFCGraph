---
id: UNC@20.15.2@MMLCommand@DSP WLRIID
type: MMLCommand
name: DSP WLRIID（显示无线路由IID信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRIID
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由相关信息
status: active
---

# DSP WLRIID（显示无线路由IID信息）

## 功能

该命令用于显示无线路由IID信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WLRIID]] · 无线路由IID信息（WLRIID）

## 使用实例

显示无线路由IID信息：

```
DSP WLRIID:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      路由IID  =  0xa000023
    原始下一跳 =  10.0.0.1
         标识  =  D
         组ID  =  1
下一跳VPN名字  =  _public_
           TP  =  1
      TB high  =  1
       TB low  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-WLRIID.md`
