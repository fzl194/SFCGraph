---
id: UDG@20.15.2@MMLCommand@LST HBUSRATTRCONF
type: MMLCommand
name: LST HBUSRATTRCONF（查询高带宽用户属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HBUSRATTRCONF
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级用户匹配
- 高带宽用户属性
status: active
---

# LST HBUSRATTRCONF（查询高带宽用户属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询高带宽用户属性。

## 注意事项

如果不输入高带宽用户属性名称，表示查询系统中所有高带宽用户属性。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONFNAME | 高带宽用户属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置高带宽用户属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HBUSRATTRCONF]] · 高带宽用户属性（HBUSRATTRCONF）

## 使用实例

- 查询名称为hbuser的高带宽用户属性：
  ```
  LST HBUSRATTRCONF: CONFNAME="hbuser";
  ```
  ```
  %%
  RETCODE = 0  操作成功

  高带宽用户属性
  --------------
  高带宽用户属性名称  =  hbuser
       过滤条件名称1  =  UsrAttrCondNm1
       过滤条件名称2  =  NULL
       过滤条件名称3  =  NULL
       过滤条件名称4  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有高带宽用户属性：
  ```
  LST HBUSRATTRCONF:;
  ```
  ```
  %%
  RETCODE = 0  操作成功

  高带宽用户属性
  --------------
  高带宽用户属性名称  过滤条件名称1   过滤条件名称2  过滤条件名称3  过滤条件名称4  

  conf1               UsrAttrCondNm1  NULL           NULL           NULL           
  hbuser              UsrAttrCondNm1  NULL           NULL           NULL           
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HBUSRATTRCONF.md`
