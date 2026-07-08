---
id: UNC@20.15.2@MMLCommand@DSP NGTZLST
type: MMLCommand
name: DSP NGTZLST（显示5G多时区参数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGTZLST
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 多时区管理
- 显示5G多时区参数
status: active
---

# DSP NGTZLST（显示5G多时区参数）

## 功能

**适用NF：AMF**

此命令用于查询某个时区是否进入夏令时。

## 注意事项

此命令必须携带TZID，TZID的取值范围为1~24。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TZID | 时区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询时区信息的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~24。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTZLST]] · 5G多时区参数（NGTZLST）

## 使用实例

查询“时区标识”为“1”的时区信息，执行如下命令：

```
%%DSP NGTZLST: TZID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
          时区标识  =  1
              时区  =  GMT+01:00
夏令时偏移量(小时)  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGTZLST.md`
