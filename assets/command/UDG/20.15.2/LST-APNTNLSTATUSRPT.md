---
id: UDG@20.15.2@MMLCommand@LST APNTNLSTATUSRPT
type: MMLCommand
name: LST APNTNLSTATUSRPT（查询隧道状态上报开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNTNLSTATUSRPT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN N6隧道状态上报
status: active
---

# LST APNTNLSTATUSRPT（查询隧道状态上报开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UPF与DN间隧道链路状态上报功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTNLSTATUSRPT]] · 隧道状态上报开关（APNTNLSTATUSRPT）

## 使用实例

- 显示指定APN实例隧道状态上报开关：
  ```
  LST APNTNLSTATUSRPT: APN="huawei.com";
  ```
  ```

  RETCODE = 0 操作成功。

  隧道状态上报功能开关
  --------------------
               APN  =  huawei.com
  隧道状态上报开关  =  使能
  (结果个数 = 1)

  ---    END
  ```
- 查询整机所有APN实例的隧道链路状态上报开关：
  ```
  LST APNTNLSTATUSRPT:;
  ```
  ```

  RETCODE = 0 操作成功。

  隧道状态上报功能开关
  --------------------
  APN         隧道状态上报开关  

  huawei.com     使能              
  example.com   使能              
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNTNLSTATUSRPT.md`
