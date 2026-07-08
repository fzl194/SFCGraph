---
id: UDG@20.15.2@MMLCommand@LST ACL
type: MMLCommand
name: LST ACL（查询ACL）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACL
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
- ACL
status: active
---

# LST ACL（查询ACL）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询系统当前配置的所有ACL配置信息，或根据名称查询对应的ACL配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACL]] · ACL（ACL）

## 使用实例

- 假如运营商需要查询名为“testacl1”的ACL配置：
  ```
  LST ACL: ACLNAME="testacl1";
  ```
  ```

  RETCODE = 0  操作成功。

  ACL信息
  -------
   ACL名称  =  testacl1
  匹配方式  =  自动排序
  生效标识  =  否
  配置域名称 = test1
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询系统配置的所有ACL信息：
  ```
  LST ACL:;
  ```
  ```

  RETCODE = 0  操作成功。

  ACL信息
  -------
  ACL名称     匹配方式    生效标识    配置域名称

  acl         自动排序    是      test1
  testacl1    自动排序    是      test1
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ACL.md`
