---
id: UNC@20.15.2@MMLCommand@LST DNAREABINDS1TAI
type: MMLCommand
name: LST DNAREABINDS1TAI（查询DNAI服务区名称绑定的4G TAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAREABINDS1TAI
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI位置绑定区域管理
status: active
---

# LST DNAREABINDS1TAI（查询DNAI服务区名称绑定的4G TAI范围）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询DNAI服务区名称绑定的4G TAI范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST DNAREA查询结果中的AREANAME保持一致，且对应的AREATYPE取值应为S1TAI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAREABINDS1TAI]] · DNAI服务区名称绑定的4G TAI范围（DNAREABINDS1TAI）

## 使用实例

- 查询UPF服务区名称为"DNAREA1"的区域绑定的TAI。 LST DNAREABINDS1TAI: AREANAME="DNAREA1";
  ```
  %%LST DNAREABINDS1TAI: AREANAME="DNAREA1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                     DNAI服务区域名称  =  dnarea1
  DNAI服务区名称支持4G TAI范围的起始值  =  460010001
  DNAI服务区名称支持4G TAI范围的结束值  =  460011234
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称绑定的TAI。 LST DNAREABINDS1TAI:;
  ```
  %%LST DNAREABINDS1TAI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNAI服务区域名称  DNAI服务区名称支持4G TAI范围的起始值  DNAI服务区名称支持4G TAI范围的结束值  

  dnarea1           460010001                          460011234                          
  dnarea3           460011234                          460012345                          
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNAI服务区名称绑定的4G-TAI范围（LST-DNAREABINDS1TAI）_16851080.md`
