---
id: UDG@20.15.2@MMLCommand@LST RULEBINDSRVS
type: MMLCommand
name: LST RULEBINDSRVS（查询业务统计规则绑定配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RULEBINDSRVS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务统计实例对象绑定规则
status: active
---

# LST RULEBINDSRVS（查询业务统计规则绑定配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定ServiceStat实例下Rule的绑定信息。

## 注意事项

该命令支持批量查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVSTATNAME | 业务统计名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RULEBINDSRVS]] · 业务统计规则绑定配置（RULEBINDSRVS）

## 使用实例

- 假如运营商希望查看基于业务的性能统计配置“stat1”所绑定的Rule对象：
  ```
  LST RULEBINDSRVS: SRVSTATNAME="stat1";
  ```
  ```

  RETCODE = 0  操作成功。

  业务统计规则绑定信息
  --------------------
  业务统计名称    规则名称    策略类型

  stat1           rule1       PCC     
  stat1           rule2       PCC     
  stat1           rule3       PCC     
  (结果个数 = 3)
  ---    END
  ```
- 假如运营商希望查询所有基于业务的性能统计配置所绑定的Rule对象：
  ```
  LST RULEBINDSRVS:;
  ```
  ```

  RETCODE = 0  操作成功。

  业务统计规则绑定信息
  --------------------
  业务统计名称    规则名称    策略类型

  stat1           rule1       PCC     
  stat1           rule2       PCC     
  stat1           rule3       PCC     
  stat2           rule1       PCC     
  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RULEBINDSRVS.md`
