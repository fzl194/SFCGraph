---
id: UDG@20.15.2@MMLCommand@LST IMSIBINDPOD
type: MMLCommand
name: LST IMSIBINDPOD（查询IMSI和Pod绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IMSIBINDPOD
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- Imsi绑定Pod
status: active
---

# LST IMSIBINDPOD（查询IMSI和Pod绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询IMSI和POD的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIBINDPOD]] · IMSI和Pod的绑定关系（IMSIBINDPOD）

## 使用实例

- 显示指定IMSI与POD的绑定关系：
  ```
  LST IMSIBINDPOD: IMSI="123456782";
  ```
  ```

  RETCODE = 0  Operation succeeded

  The imsi Pod binding information
  --------------------------------
      IMSI  =  123456782
  Pod Name  =  ssgpod-0
  (Number of results = 1)
  ```
- 查询整机IMSI与POD的绑定关系：
  ```
  LST IMSIBINDPOD:;
  ```
  ```

  RETCODE = 0  Operation succeeded

  The imsi Pod binding information
  --------------------------------
  IMSI       Pod Name             

  123456781  ssgpod-0
  123456782  ssgpod-0
  123456789  ssgpod-0
  (Number of results = 3)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IMSIBINDPOD.md`
