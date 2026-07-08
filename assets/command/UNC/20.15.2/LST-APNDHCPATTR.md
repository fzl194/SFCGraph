---
id: UNC@20.15.2@MMLCommand@LST APNDHCPATTR
type: MMLCommand
name: LST APNDHCPATTR（查询APN DHCP属性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNDHCPATTR
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN的DHCP属性
status: active
---

# LST APNDHCPATTR（查询APN DHCP属性配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于查询APN的DHCP相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNDHCPATTR]] · APN DHCP属性配置（APNDHCPATTR）

## 使用实例

- 假设用户要查询所有APN下配置的DHCP相关信息：
  ```
  %%LST APNDHCPATTR:;%%
  RETCODE = 0 操作成功

  结果如下
  --------
  APN名称 DHCPv4延迟分配 租约无限 租约天数(天) 租约小时数(小时) 租约分钟数(分钟) DHCPv6无状态

  0168apn1.com          使能                         不使能         1                0                  0                  不使能                   
  0168apn2.com          使能                         不使能         1                0                  0                  不使能  
  a.mnc003.mcc460.gprs  使能                         不使能         1                0                  0                  不使能         
  huawei.com            使能                         不使能         1                0                  0                  不使能
  (结果个数 = 4)

  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的DHCP相关信息：
  ```
  %%LST APNDHCPATTR: APN="huawei.com";%%
  RETCODE = 0 操作成功

  结果如下
  --------
               APN名称  =  huawei.com
         DHCPv4延迟分配 = 使能
               租约无限 = 不使能
           租约天数(天) = 1
       租约小时数(小时) = 0
       租约分钟数(分钟) = 0
           DHCPv6无状态 = 不使能
  (结果个数 = 1)

  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNDHCPATTR.md`
