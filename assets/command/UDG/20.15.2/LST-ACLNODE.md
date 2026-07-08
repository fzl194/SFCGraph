---
id: UDG@20.15.2@MMLCommand@LST ACLNODE
type: MMLCommand
name: LST ACLNODE（查询ACL节点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLNODE
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL节点
status: active
---

# LST ACLNODE（查询ACL节点）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询所有配置的ACL节点信息，或者查询指定的ACL节点配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNODENAME | ACL节点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ACL节点（ACLNODE）](configobject/UDG/20.15.2/ACLNODE.md)

## 使用实例

- 假如运营商需要查询名为“testaclnode1”的ACL节点配置：
  ```
  LST ACLNODE: ACLNODENAME="testaclnode1";
  ```
  ```

  RETCODE = 0  操作成功。

  ACL节点信息
  -----------
     ACL节点名称  =  testaclnode1
      过滤器名字  =  filter1
        动作类型  =  门控
        门控动作  =  Pass
      重标记类型  =  NULL
        重标记值  =  NULL
        重标记类  =  NULL
    重定向IP版本  =  IPv4
  重定向IPv4地址  =  0.0.0.0
  重定向IPv6地址  =  ::
        生效标识  =  是
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询系统配置的所有ACL节点信息：
  ```
  LST ACLNODE:;
  ```
  ```

  RETCODE = 0  操作成功。

  ACL节点信息
  -----------
  ACL节点名称     过滤器名字    动作类型    门控动作    重标记类型    重标记值    重标记类    重定向IP版本    重定向IPv4地址    重定向IPv6地址    生效标识

  aclnode2        filter1       重定向      Pass        NULL          NULL        NULL        IPv4            10.10.0.1         ::                否      
  testaclnode1    filter1       门控        Pass        NULL          NULL        NULL        IPv4            0.0.0.0           ::                是      
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ACL节点（LST-ACLNODE）_86526723.md`
