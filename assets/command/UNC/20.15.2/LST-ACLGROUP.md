---
id: UNC@20.15.2@MMLCommand@LST ACLGROUP
type: MMLCommand
name: LST ACLGROUP（查询ACL规则组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACLGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- ACL规则组
status: active
---

# LST ACLGROUP（查询ACL规则组配置）

## 功能

该命令用于查询系统内已经配置的ACL规则组的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是1000～1999（接口ACL），2000～2999（基本ACL），3000～3999（高级ACL），4000～4999（以太ACL）。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLGROUP]] · ACL规则匹配计数（ACLGROUP）

## 使用实例

- 查询当前设备上所有的规则组信息，不输入ACLNAME：
  ```
  LST ACLGROUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  ACL规则组标识    规则组步长    规则组类型    规则的匹配顺序                    规则组描述

  1000             5             接口型ACL     规则组下的规则按照配置优先排序    NULL
  2000             5             基本ACL       规则组下的规则按照配置优先排序    NULL
  3000             5             高级ACL       规则组下的规则按照配置优先排序    NULL
  4000             5             以太ACL       规则组下的规则按照配置优先排序    NULL
  (结果个数 = 4)
  ---    END
  ```
- 查询规则组1000的信息：
  ```
  LST ACLGROUP: ACLNAME="1000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
   ACL规则组标识  =  1000
      规则组步长  =  5
      规则组类型  =  接口型ACL
  规则的匹配顺序  =  规则组下的规则按照配置优先排序
      规则组描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ACLGROUP.md`
