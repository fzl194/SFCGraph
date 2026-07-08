---
id: UNC@20.15.2@MMLCommand@LST BACKOFFTIME
type: MMLCommand
name: LST BACKOFFTIME（查询Back-off Time信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BACKOFFTIME
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- Back-off Time信息
status: active
---

# LST BACKOFFTIME（查询Back-off Time信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查看APN下的Back-off Time参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BACKOFFTIME]] · Back-off Time信息（BACKOFFTIME）

## 使用实例

查询APN为“apn”下的Back-off Time配置：

```
%%LST BACKOFFTIME: APNNAME="apn";%%
RETCODE = 0  操作成功

结果如下
--------
                           APN名称  =  apn
   系统过载场景下Back-off Time开关  =  不使能
    APN拥塞场景下Back-off Time开关  =  不使能
Back-off Time启动激活成功率阈值(%)  =  70
     Back-off Time控制检测时长(秒)  =  15
    Back-off Time恢复激活成功率(%)  =  80
     Back-off Time恢复检测时长(秒)  =  15
	 是否继承全局Back-off时长   =  否
                  Back-off时长(秒)  =  600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BACKOFFTIME.md`
