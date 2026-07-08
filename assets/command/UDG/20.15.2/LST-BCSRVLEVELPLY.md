---
id: UDG@20.15.2@MMLCommand@LST BCSRVLEVELPLY
type: MMLCommand
name: LST BCSRVLEVELPLY（查询带宽管理控制器业务级别策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BCSRVLEVELPLY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理控制器业务级别策略
status: active
---

# LST BCSRVLEVELPLY（查询带宽管理控制器业务级别策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定BWM控制器下，特定ServiceLevel的业务流量保证带宽比例和峰值带宽比例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMCNAME | 带宽管理控制器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示带宽管理控制器的名字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：不输入此参数表示查询所有“BCSrvLevelPly”配置。输入“ServiceLevel”参数时必须输入“BwmcName”参数。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定使用同一控制器的不同业务流间的优先级，值越小优先级越高。如果配置优先级，优先保证高优先级的带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：不输入此参数表示查询指定BwmController下所有业务级别的“BCSrvLevelPly”配置。 |

## 操作的配置对象

- [带宽管理控策略制器业务级别（BCSRVLEVELPLY）](configobject/UDG/20.15.2/BCSRVLEVELPLY.md)

## 使用实例

查询带宽管理控制器“bc1”下业务级别为1的控制策略：

```
LST BCSRVLEVELPLY: BWMCNAME="bc1", SERVICELEVEL=1;
```

```

RETCODE = 0  操作成功
带宽管理控制器业务级别策略信息
-----------------------------------------------
带宽管理控制器名称  =  bc1
          业务级别  = 1
  承诺信息速率比例  = 0
  流量整形速率比例  = 0
  峰值信息速率比例  = 10000
        最大丢包率  = 10000
      最大增加时延  = NULL
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询带宽管理控制器业务级别策略（LST-BCSRVLEVELPLY）_92618466.md`
