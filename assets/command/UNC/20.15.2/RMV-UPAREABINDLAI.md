---
id: UNC@20.15.2@MMLCommand@RMV UPAREABINDLAI
type: MMLCommand
name: RMV UPAREABINDLAI（删除UPF服务区名称绑定的LAI范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPAREABINDLAI
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- LAI绑定UP区域
status: active
---

# RMV UPAREABINDLAI（删除UPF服务区名称绑定的LAI范围）

## 功能

**适用NF：GGSN**

该命令用于删除UPF服务区名称对应绑定的LAI范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置UPF服务区的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为LAI。 |
| BEGINLAI | UPF服务区名称绑定的LAI范围的起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定的LAI范围的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。前5位数或者6位数为移动国家号(MCC)+移动网号(MNC)，为10进制数；后4位数为位置区号码(LAC)，为16进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>LAI范围的结束值需要不小于LAI范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPAREABINDLAI]] · UPF服务区名称绑定的LAI范围（UPAREABINDLAI）

## 使用实例

删除UPF服务区名称为“UPAREA1”的LAI绑定范围460010001~460011111。

```
RMV UPAREABINDLAI: AREANAME="UPAREA1", BEGINLAI="460010001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPAREABINDLAI.md`
