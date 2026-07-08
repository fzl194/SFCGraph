---
id: UNC@20.15.2@MMLCommand@LST PERFNS
type: MMLCommand
name: LST PERFNS（查询切片性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFNS
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST PERFNS（查询切片性能统计对象）

## 功能

**适用NF：AMF、SMF**

该命令用于显示性能统计对象的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SNSSAI | 网络切片 | 可选必选说明：可选参数<br>参数含义：该参数标识切片信息，由切片业务类型和切片细分标识组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是8~10。网络切片输入格式为SST-SD。SST输入长度范围是1~3，只允许输入十进制数字（0-9），除0之外不能以0开头，对应十进制数取值范围是0~255；SD输入长度为6，采用十六进制表示，只能由数字（0-9），字母（A-F、a-f）组成，字母大小写不敏感。<br>默认值：无<br>配置原则：<br>网络已支持的切片（ADD PLMNNS配置）会自动添加到PERFNS中，不需要人工配置。执行ADD PERFNS命令时只能配置ADD PLMNNS命令没有配置过的切片。若PERFNS记录数已达到最大规格，则随后执行ADD PLMNNS命令添加的新切片信息不会再自动同步到PERFNS中。 |
| SOURCE | 记录来源 | 可选必选说明：可选参数<br>参数含义：该参数用于标识切片信息的配置来源。配置来源包括系统同步和人工配置。<br>数据来源：本端规划<br>取值范围：<br>- “AUTO_SYNC（自动同步）”：自动同步<br>- “MANUAL（人工配置）”：人工配置<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNS]] · 切片性能统计对象（PERFNS）

## 使用实例

显示切片性能统计对象的配置信息：

```
%%LST PERFNS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
网络切片       记录来源  

125-4DABBB     人工配置
25-FFFFFF      自动同步   
7-FFFFFF       自动同步      
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFNS.md`
