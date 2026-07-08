---
id: UNC@20.15.2@MMLCommand@DSP WLRIFFLOWRULE6
type: MMLCommand
name: DSP WLRIFFLOWRULE6（查询无线路由IPv6接口引流表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRIFFLOWRULE6
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示引流表统计信息
status: active
---

# DSP WLRIFFLOWRULE6（查询无线路由IPv6接口引流表信息）

## 功能

该命令用于查询无线路由接收到的IPv6接口引流表信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACE | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@WLRIFFLOWRULE6]] · 无线路由IPv6接口引流表信息（WLRIFFLOWRULE6）

## 使用实例

查询无线路由接收的IPv6接口引流表信息：

```
DSP WLRIFFLOWRULE6:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
     VPN名称   =  vrf1
     接口名称  =  Tunnel1
       下一跳  =  2001:DB8::1
       序列号  =  0
        属性1  =  1
        属性2  =  0
        属性3  =  0
        属性4  =  0
        属性5  =  0
        属性6  =  0
        属性7  =  0
        属性8  =  0
        版本号 =  4
       标记位  =  0
     对端地址  =  2001:DB8::5
      PAE组ID  =  65
       间接ID  =  0x1
         类型  =  0
   策略组标识  =  0
是否发送给FES  =  TRUE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-WLRIFFLOWRULE6.md`
