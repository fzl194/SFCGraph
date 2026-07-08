---
id: UNC@20.15.2@MMLCommand@DSP UPFAULTAPNCACHE
type: MMLCommand
name: DSP UPFAULTAPNCACHE（显示故障APN信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPFAULTAPNCACHE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 用户面故障管理
status: active
---

# DSP UPFAULTAPNCACHE（显示故障APN信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于显示用户面故障APN信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFAULTAPNCACHE]] · 故障APN信息（UPFAULTAPNCACHE）

## 使用实例

查询所有用户面故障APN信息：

```
%%DSP UPFAULTAPNCACHE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
         UPF实例标识  =  upf_instance_1
         UPF描述名称  =  NULL
             APN名称  =  huawei.com
            故障时间  =  2022-12-12T11:37:22+08:00
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-UPFAULTAPNCACHE.md`
