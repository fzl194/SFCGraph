---
id: UDG@20.15.2@MMLCommand@LST URRGROUP
type: MMLCommand
name: LST URRGROUP（查询URR组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: URRGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 使用率上报规则组
status: active
---

# LST URRGROUP（查询URR组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询使用量上报规则组。当运营商希望查询使用量上报规则组时，则执行该命令。

## 注意事项

如果不输入使用量上报规则组名称，表示查询系统中所有计费属性。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRGROUPNAME | 使用量上报规则组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置使用量上报规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@URRGROUP]] · URR组（URRGROUP）

## 使用实例

- 假如运营商需要查询名称为urrgroup1的使用量上报规则组：
  ```
  LST URRGROUP: URRGROUPNAME="urrgroup1";
  ```
  ```

  RETCODE = 0  操作成功。

  URR组信息：
  -----------
  使用量上报规则组名称  =  urrgroup1
      上行发起URR名称1  =  uponurr
      上行发起URR名称2  =  upoffurr
      上行发起URR名称3  =  NULL
      下行发起URR名称1  =  downonurr
      下行发起URR名称2  =  downoffurr
      下行发起URR名称3  =  NULL
            配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有的使用量上报规则组：
  ```
  LST URRGROUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  URR组信息：
  -----------
  使用量上报规则组名称    上行发起URR名称1    上行发起URR名称2    上行发起URR名称3    下行发起URR名称1    下行发起URR名称2    下行发起URR名称3    配置域名称

  urrgroup1               uponurr             upoffurr            NULL                downonurr           downoffurr          NULL                    NULL
  urrgroup2               uponurr             NULL                NULL                downonurr           NULL                NULL                    NULL
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-URRGROUP.md`
