---
id: UDG@20.15.2@MMLCommand@DSP WLRFLOWRULE6
type: MMLCommand
name: DSP WLRFLOWRULE6（查询IPv6引流表信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRFLOWRULE6
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

# DSP WLRFLOWRULE6（查询IPv6引流表信息）

## 功能

该命令用来查询IPv6引流表信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCIP | 源IP | 可选必选说明：可选参数<br>参数含义：该参数用来表示源IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。IPv6地址。<br>默认值：无 |
| DSTIP | 目的IP | 可选必选说明：可选参数<br>参数含义：该参数用来表示目的IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。IPv6地址。<br>默认值：无 |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WLRFLOWRULE6]] · IPv6引流表信息（WLRFLOWRULE6）

## 使用实例

查询IPv6引流表信息：

```
DSP WLRFLOWRULE6:;
```

```

RETCODE = 0  操作成功.

结果如下
------------------------
    引流表组ID  =  4
        序列号  =  4
          源IP  =  2001:DB8::1
    源前缀长度  =  64
        目的IP  =  2001:DB8::101
  目的前缀长度  =  64
      源端口号  =  4
    目的端口号  =  4
         属性1  =  4
         属性2  =  4
         属性3  =  4
         属性4  =  4
         属性5  =  4
         属性6  =  4
         属性7  =  4
         属性8  =  4
       VPN名称  =  vrf1
    平滑版本号  =  1
网络逻辑单元ID  =  0
       PAE组ID  =  4
      对端地址  =  2001:DB8::10
        用户ID  =  0
        标记位  =  0
        间接ID  =  0x1
        协议号  =  17
        规则ID  =  4
  最大源端口号  =  11
最大目的端口号  =  33
          类型  =  1
          行为  =  0
    引流表索引  =  2
 是否发送给FES  =  TRUE
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv6引流表信息（DSP-WLRFLOWRULE6）_49961042.md`
