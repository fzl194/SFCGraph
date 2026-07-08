---
id: UDG@20.15.2@MMLCommand@LST PREURLGBINDUP
type: MMLCommand
name: LST PREURLGBINDUP（查询用户模板的前缀URL组绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PREURLGBINDUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- Prefixed URL组绑定
status: active
---

# LST PREURLGBINDUP（查询用户模板的前缀URL组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询用户模板与前缀URL组的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板的前缀URL组绑定关系（PREURLGBINDUP）](configobject/UDG/20.15.2/PREURLGBINDUP.md)

## 使用实例

- 查询前缀URL组与名为testprofile的UserProfile的绑定关系：
  ```
  LST PREURLGBINDUP: USERPROFILENAME="testprofile";
  ```
  ```

  RETCODE = 0  操作成功。

  User Profile绑定Prefixed URL 组Information
  ------------------------------------------
  用户模板名称    前缀URL组名称

  testprofile     testurlgroup 
  testprofile     testurlgroup1
  (结果个数 = 2)
  ---    END
  ```
- 查询前缀URL组与UserProfile所有的绑定关系：
  ```
  LST PREURLGBINDUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  User Profile绑定Prefixed URL 组Information
  ------------------------------------------
  用户模板名称    前缀URL组名称

  testprofile     testurlgroup 
  testprofile     testurlgroup1
  testprofile2    testurlgroup2
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户模板的前缀URL组绑定关系（LST-PREURLGBINDUP）_82837413.md`
