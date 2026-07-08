---
id: UNC@20.15.2@MMLCommand@LST DNAREABINDN2CID
type: MMLCommand
name: LST DNAREABINDN2CID（查询DNAI服务区名称绑定的5G Cell ID范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAREABINDN2CID
command_category: 查询类
applicable_nf:
- SGW-C
- GGSN
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI位置绑定区域管理
status: active
---

# LST DNAREABINDN2CID（查询DNAI服务区名称绑定的5G Cell ID范围）

## 功能

**适用NF：SGW-C、GGSN、SMF、PGW-C**

该命令用于查询DNAI服务区名称绑定的5G Cell ID范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST DNAREA查询结果中的AREANAME保持一致，且对应的AREATYPE取值应为N2CID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAREABINDN2CID]] · DNAI服务区名称绑定的5G Cell ID范围（DNAREABINDN2CID）

## 使用实例

- 查询UPF服务区名称为"DNAREA1"的区域绑定的CID。 LST DNAREABINDN2CID: AREANAME="DNAREA1";
  ```
  %%LST DNAREABINDN2CID: AREANAME="DNAREA1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                      DNAI服务区域名称  =  dnarea1
  DNAI服务区名称支持5G小区范围的起始值  =  46001000001234
  DNAI服务区名称支持5G小区范围的结束值  =  46001000005678
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称绑定的CID。 LST DNAREABINDN2CID:;
  ```
  %%LST DNAREABINDN2CID:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNAI服务区域名称  DNAI服务区名称支持5G小区范围的起始值  DNAI服务区名称支持5G小区范围的结束值  

  dnarea1           46001000001234                        46001000005678                        
  dnarea4           46001000005679                        46001000006789                        
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNAI服务区名称绑定的5G-Cell-ID范围（LST-DNAREABINDN2CID）_24956632.md`
