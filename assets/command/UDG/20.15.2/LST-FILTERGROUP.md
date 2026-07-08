---
id: UDG@20.15.2@MMLCommand@LST FILTERGROUP
type: MMLCommand
name: LST FILTERGROUP（查询过滤器组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FILTERGROUP
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
- 流过滤器管理
- 过滤器组
status: active
---

# LST FILTERGROUP（查询过滤器组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询过滤器组，以及组内的过滤器绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGRPNAME | 过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FILTERGROUP]] · 过滤器组（FILTERGROUP）

## 使用实例

- 查询名称为group1的过滤器组：
  ```
  LST FILTERGROUP: FILTERGRPNAME="group1";
  ```
  ```

  RETCODE = 0 操作成功。

  过滤器组信息
  -------------
  过滤器组名称 = group1
    过滤器名称 = filter1
   配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有过滤器组配置：
  ```
  LST FILTERGROUP:;
  ```
  ```

  RETCODE = 0 操作成功。

  过滤器组信息
  ------------------
  过滤器组名称        过滤器名称    配置域名称

  group1               filter1       NULL
  group2               无效          NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询过滤器组（LST-FILTERGROUP）_95089584.md`
