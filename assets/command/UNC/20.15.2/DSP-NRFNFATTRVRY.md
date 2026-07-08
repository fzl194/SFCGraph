---
id: UNC@20.15.2@MMLCommand@DSP NRFNFATTRVRY
type: MMLCommand
name: DSP NRFNFATTRVRY（显示NF属性冲突核验记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFNFATTRVRY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF属性冲突核验
status: active
---

# DSP NRFNFATTRVRY（显示NF属性冲突核验记录）

## 功能

**适用NF：NRF**

该命令用于查询某个NF的属性冲突核验结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示进行属性冲突核验的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。 |

## 操作的配置对象

- [操作执行NF属性冲突核验（NRFNFATTRVRY）](configobject/UNC/20.15.2/NRFNFATTRVRY.md)

## 使用实例

查询某个NF的属性冲突核验结果：

```
DSP NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
%%DSP NRFNFATTRVRY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

结果如下
--------
    NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
      核验结果  =  The check is passed.
    NF更新时间  =  2021-03-16 17:59:42
      执行时间  =  2021-03-16 20:17:35
  消耗时长(秒)  =  1
       Pod名称  =  uncpod-0
      核验进度  =  VerifiedNum:2;TotalNum:2;Percentage:100%;
  属性冲突类型  =  No Conflict
NF实例标识集合  =  NULL
下一跳NRFGroup  =  NULL
    NF冲突属性  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NF属性冲突核验记录（DSP-NRFNFATTRVRY）_35519269.md`
