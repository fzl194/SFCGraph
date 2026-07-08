---
id: UNC@20.15.2@MMLCommand@LST OSPFAREAFILTER
type: MMLCommand
name: LST OSPFAREAFILTER（查询区域过滤策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFAREAFILTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域过滤策略配置
status: active
---

# LST OSPFAREAFILTER（查询区域过滤策略配置）

## 功能

该命令用于查询区域过滤策略配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域ID | 可选必选说明：可选参数<br>参数含义：区域ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| FILTERTYPE | 过滤方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤规则类型 | 可选必选说明：可选参数<br>参数含义：过滤规则类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL名称。<br>- ip_prefix：IP前缀列表。<br>- route_policy：路由策略名。<br>- acl_num：ACL号。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFAREAFILTER]] · 区域过滤策略配置（OSPFAREAFILTER）

## 使用实例

查询区域过滤策略配置：

```
LST OSPFAREAFILTER:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
         OSPF进程号  =  1
             区域ID  =  0.0.0.0
           拓扑标识  =  基础类型
           过滤方向  =  引入方向的过滤
       过滤规则类型  =  路由策略名
     ACL名称或ACL号  =  NULL
 IP前缀过滤策略名称  =  NULL
       路由策略名称  =  RtPolicy
包括ABR Summary LSA  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询区域过滤策略配置（LST-OSPFAREAFILTER）_49962106.md`
