---
id: UDG@20.15.2@MMLCommand@LST HEADENRATTYPE
type: MMLCommand
name: LST HEADENRATTYPE（查询头增强RAT类型定义）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HEADENRATTYPE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强RAT类型
status: active
---

# LST HEADENRATTYPE（查询头增强RAT类型定义）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询头增强RAT类型定义参数，查看相应的RAT类型设置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPEVALUE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个RAT类型，查询其相应字符串的值。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- RESERVED：预留RAT类型。<br>- UTRAN：无线接入类型为UMTS陆地无线接入网。<br>- GERAN：无线接入类型为GSM/EDGE无线接入网。<br>- WLAN：无线接入类型为无线局域网。<br>- GAN：无线接入类型为通用接入网络。<br>- HSPAE：无线接入类型为增强型高速分组接入。<br>- EUTRAN：无线接入类型为演进UMTS陆地无线接入网。<br>- VIRTUAL：无线接入类型为Virtual。<br>- EUTRANNBIOT：无线接入类型为EUTRAN-NB-IoT。<br>- LTEM：无线接入类型为LTE-M。<br>- NR：无线接入类型为NR。<br>- REDCAPNR：无线接入类型为RedCap-NR。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [头增强RAT类型定义（HEADENRATTYPE）](configobject/UDG/20.15.2/HEADENRATTYPE.md)

## 使用实例

- 假如运营商希望查看所有类型的头增强RAT参数：
  ```
  LST HEADENRATTYPE:;
  ```
  ```

  RETCODE = 0  操作成功。

  头增强RAT类型定义信息
  ---------------------
  用户定义的预留RAT类型字符串 = RESERVED
  用户定义的UTRAN类型字符串 = UTRAN
  用户定义的GERAN类型字符串 = GERAN
  用户定义的WLAN类型字符串 = WLAN
  用户定义的GAN类型字符串 = GAN
  用户定义的HAPAEvolution类型字符串 = HSPA Evolution
  用户定义的EUTRAN类型字符串 = EUTRAN
  用户定义的Virtual类型字符串 = Virtual
  用户定义的LTE-M类型字符串 = LTE-M
  用户定义的NR类型字符串 = NR
  用户定义的EUTRAN-NB-IoT类型字符串 = EUTRAN-NB-IoT
  用户定义的RedCap-NR类型字符串 = REDCAP
  (结果个数 = 1)
  --- END
  ```
- 假如运营商希望查看RAT类型为WLAN的头增强RAT参数：
  ```
  LST HEADENRATTYPE: RATTYPEVALUE=WLAN;
  ```
  ```

  RETCODE = 0  操作成功。

  头增强RAT类型定义信息
  ---------------------
  用户定义的WLAN类型字符串  =  WLAN
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询头增强RAT类型定义（LST-HEADENRATTYPE）_82837510.md`
