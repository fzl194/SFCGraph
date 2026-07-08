---
id: UNC@20.15.2@MMLCommand@LST UPAREABINDS1TAI
type: MMLCommand
name: LST UPAREABINDS1TAI（查询UPF服务区名称绑定的4G TAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPAREABINDS1TAI
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- TAI绑定UP区域
status: active
---

# LST UPAREABINDS1TAI（查询UPF服务区名称绑定的4G TAI范围）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询UPF服务区名称绑定的4G TAI范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为S1TAI。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPAREABINDS1TAI]] · UPF服务区名称绑定的4G TAI范围（UPAREABINDS1TAI）

## 使用实例

- 查询UPF服务区名称为"UPAREA1"的区域绑定的4G TAI。 LST UPAREABINDS1TAI: AREANAME="UPAREA1";
  ```
  %%LST UPAREABINDS1TAI: AREANAME="UPAREA1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
                     UPF服务区名称  =  uparea1
  UPF服务区名称绑定4G TAI范围起始值  =  123010001
  UPF服务区名称绑定4G TAI范围结束值  =  123011111
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称绑定的4G TAI。 LST UPAREABINDS1TAI:;
  ```
  %%LST UPAREABINDS1TAI:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  UPF服务区名称  UPF服务区名称绑定4G TAI范围起始值  UPF服务区名称绑定4G TAI范围结束值
 
  s1area1001     123030000                         123030009               
  s1area1001     1230310000                        1230310009              
  uparea1        123010001                         123011111               
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPAREABINDS1TAI.md`
