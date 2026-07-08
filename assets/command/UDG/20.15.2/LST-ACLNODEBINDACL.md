---
id: UDG@20.15.2@MMLCommand@LST ACLNODEBINDACL
type: MMLCommand
name: LST ACLNODEBINDACL（查询Acl节点绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLNODEBINDACL
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
- ACL节点绑定ACL
status: active
---

# LST ACLNODEBINDACL（查询Acl节点绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询所有配置的ACL节点绑定关系，或者指定的ACL名称下的节点绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Acl节点绑定关系（ACLNODEBINDACL）](configobject/UDG/20.15.2/ACLNODEBINDACL.md)

## 使用实例

- 假如运营商需要查询ACL“testacl1”下ACL节点绑定信息：
  ```
  LST ACLNODEBINDACL: ACLNAME="testacl1";
  ```
  ```

  RETCODE = 0  操作成功。

  ACL节点绑定关系信息
  -------------------
      ACL名称  =  testacl1
  ACL节点名称  =  testaclnode1
       优先级  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询系统当前所有的ACL节点绑定信息：
  ```
  LST ACLNODEBINDACL:;
  ```
  ```

  RETCODE = 0  操作成功。

  ACL节点绑定关系信息
  -------------------
  ACL名称     ACL节点名称     优先级

  acl         testaclnode1    NULL  
  testacl1    testaclnode1    NULL  
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Acl节点绑定关系（LST-ACLNODEBINDACL）_82837737.md`
