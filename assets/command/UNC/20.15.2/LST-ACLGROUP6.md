---
id: UNC@20.15.2@MMLCommand@LST ACLGROUP6
type: MMLCommand
name: LST ACLGROUP6（查询IPv6 ACL规则组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACLGROUP6
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- IPv6 ACL规则组
status: active
---

# LST ACLGROUP6（查询IPv6 ACL规则组配置）

## 功能

该命令用于查询系统内已经配置的IPv6 ACL规则组的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是2000～2999（基本IPv6 ACL），3000～3999（高级IPv6 ACL）。<br>默认值：无 |

## 操作的配置对象

- [IPv6 ACL规则匹配计数（ACLGROUP6）](configobject/UNC/20.15.2/ACLGROUP6.md)

## 使用实例

- 查询当前设备上所有的IPv6 ACL规则组信息，不输入ACLNAME：
  ```
  LST ACLGROUP6:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IPv6 ACL规则组标识    规则组步长    规则组类型    规则的匹配顺序                    规则组描述

  2000                  5             基本ACL       规则组下的规则按照配置优先排序    NULL
  3000                  5             高级ACL       规则组下的规则按照配置优先排序    NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询IPv6 ACL规则组2005的信息：
  ```
  LST ACLGROUP6:ACLNAME="3000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IPv6 ACL规则组标识  =  3000
          规则组步长  =  5
          规则组类型  =  高级ACL
      规则的匹配顺序  =  规则组下的规则按照配置优先排序
          规则组描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6-ACL规则组配置（LST-ACLGROUP6）_00865729.md`
