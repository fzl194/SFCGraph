---
id: UNC@20.15.2@MMLCommand@LST VIRTUALAPNRULE
type: MMLCommand
name: LST VIRTUALAPNRULE（查询虚拟APN映射策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VIRTUALAPNRULE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 虚拟APN映射策略
status: active
---

# LST VIRTUALAPNRULE（查询虚拟APN映射策略配置）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用来查询指定虚拟APN的匹配规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VIRTUALAPN | 虚拟APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例为虚拟APN。该APN必须是系统已经配置的APN，并且该APN下的VIRTUALAPN字段是使能的。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：<br>该参数的取值必须在ADD APN中进行配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VIRTUALAPNRULE]] · 虚拟APN映射策略配置（VIRTUALAPNRULE）

## 使用实例

查询Virtual APN为0168apn10.com的虚拟APN的配置信息：

```
%%LST VIRTUALAPNRULE:;%%
RETCODE = 0  操作成功

结果如下
--------
             虚拟APN名称  =  0168apn10.com
                映射方式  =  多参数
                  优先级  =  1
            计费属性模式  =  空
                  映射值  =  NULL
              计费属性值  =  NULL
计费特征掩码和优先级开关  =  不使能
            计费特征掩码  =  NULL
          计费特征优先级  =  0
            无线接入类型  =  空
                漫游状态  =  空
             真实APN开关  =  不使能
                    IMSI  =  NULL
                  MSISDN  =  NULL
                    IMEI  =  NULL
                 LAC组名  =  NULL
                 TAC组名  =  tacgroup3
                 RAC组名  =  NULL
      Serving Node组名称  =  NULL
                    PLMN  =  NULL
                 PCO开关  =  不使能
                    域名  =  NULL
                选择模式  =  空
            切片业务类型  =  0
            切片细分标识  =  FFFFFF
             真实APN名称  =  huawei.com
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VIRTUALAPNRULE.md`
