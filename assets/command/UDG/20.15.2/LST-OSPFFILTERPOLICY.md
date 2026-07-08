---
id: UDG@20.15.2@MMLCommand@LST OSPFFILTERPOLICY
type: MMLCommand
name: LST OSPFFILTERPOLICY（查询OSPF过滤策略配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFFILTERPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF过滤策略配置
status: active
---

# LST OSPFFILTERPOLICY（查询OSPF过滤策略配置）

## 功能

该命令用于查询OSPF过滤策略配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| FILTERTYPE | 过滤方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤方向是import还是export。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| TYPE | 过滤规则类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定过滤类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL名称。<br>- ip_prefix：IP前缀列表。<br>- route_policy：路由策略名。<br>- acl_num：ACL号。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFFILTERPOLICY]] · OSPF过滤策略配置（OSPFFILTERPOLICY）

## 使用实例

查询OSPF过滤策略配置：

```
LST OSPFFILTERPOLICY:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
            进程号  =  1
          拓扑标识  =  0
          过滤方向  =  发布方向的过滤
      过滤规则类型  =  路由策略名
    ACL名称或ACL号  =  NULL
IP前缀过滤策略名称  =  NULL
      路由策略名称  =  123
  是否优选次优路由  =  FALSE
          协议分类  =  OSPF路由
        协议进程号  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFFILTERPOLICY.md`
