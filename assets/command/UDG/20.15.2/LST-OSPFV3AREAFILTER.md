---
id: UDG@20.15.2@MMLCommand@LST OSPFV3AREAFILTER
type: MMLCommand
name: LST OSPFV3AREAFILTER（查询OSPFv3区域过滤LSA配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3AREAFILTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域过滤LSA配置
status: active
---

# LST OSPFV3AREAFILTER（查询OSPFv3区域过滤LSA配置）

## 功能

该命令用于查询OSPFv3区域过滤LSA配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| FILTERTYPE | 过滤方向 | 可选必选说明：可选参数<br>参数含义：过滤方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤类型 | 可选必选说明：可选参数<br>参数含义：过滤规则类型(ACL名称或ACL号/IP前缀过滤策略名称)。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL6名称。<br>- ip_prefix：IPv6前缀池列表。<br>- route_policy：路由策略。<br>- acl_num：ACL号。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3区域过滤LSA配置（OSPFV3AREAFILTER）](configobject/UDG/20.15.2/OSPFV3AREAFILTER.md)

## 使用实例

查询OSPFv3区域过滤LSA配置：

```
LST OSPFV3AREAFILTER:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
  OSPFv3进程号  =  1
  OSPFv3区域号  =  0.0.0.0
      拓扑标识  =  0
      过滤方向  =  引入方向的过滤
      过滤类型  =  路由策略
ACL名称或ACL号  =  NULL
        IP前缀  =  NULL
  路由策略名称  =  RtPolicy
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3区域过滤LSA配置（LST-OSPFV3AREAFILTER）_00865865.md`
