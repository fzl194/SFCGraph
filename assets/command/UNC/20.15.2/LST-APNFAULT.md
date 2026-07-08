---
id: UNC@20.15.2@MMLCommand@LST APNFAULT
type: MMLCommand
name: LST APNFAULT（查询APN粒度的故障处理开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNFAULT
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- APN故障处理
status: active
---

# LST APNFAULT（查询APN粒度的故障处理开关）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询APN粒度的故障处理开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN粒度的故障处理开关（APNFAULT）](configobject/UNC/20.15.2/APNFAULT.md)

## 使用实例

查询APN为test下的APN故障处理的开关配置。

```
%%LST APNFAULT: APN="test";%%
RETCODE = 0	 操作成功

结果如下
--------
                      APN名称  =  huawei.com
           UP链路故障处理模式  =  检测到故障后隔离
SMF是否支持用户面链路故障恢复  =  使能 
        辅锚点UPF迁移功能开关  =  使能
(结果个数 = 1) 

---	   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN粒度的故障处理开关（LST-APNFAULT）_98629445.md`
