---
id: UNC@20.15.2@MMLCommand@LST APNAREA
type: MMLCommand
name: LST APNAREA（查询APN相关服务区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNAREA
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN相关服务区域管理
status: active
---

# LST APNAREA（查询APN相关服务区域）

## 功能

**适用NF：SMF**

该命令用于查询APN相关服务区域。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | APN相关服务区域 | 可选必选说明：可选参数<br>参数含义：该参数用于配置APN相关服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNAREA]] · APN相关服务区域（APNAREA）

## 使用实例

- 查询区域名称为"dnnarea1"的APN服务区域信息。
  ```
  %%LST APNAREA:AREANAME="dnnarea1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    APN相关服务区域  =  dnnarea1
    APN服务区域类型  =  5G类型的TAI
  (结果个数 = 1)
  ```
- 查询所有的APN服务区域信息。
  ```
  %%LST APNAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN相关服务区域  APN服务区域类型  

  dnnarea1           5G类型的TAI       
  dnnarea2           5G类型的TAI   
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNAREA.md`
