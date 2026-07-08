---
id: UNC@20.15.2@MMLCommand@DSP COMBASEHEALTH
type: MMLCommand
name: DSP COMBASEHEALTH（显示Base平面通信质量）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMBASEHEALTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# DSP COMBASEHEALTH（显示Base平面通信质量）

## 功能

该命令用于显示Base平面通信质量。

## 注意事项

该命令依赖于 [**SET COMBASEHEALTH**](设置Base平面的亚健康检测参数（SET COMBASEHEALTH）_32217476.md) 命令，需要在使用 [**SET COMBASEHEALTH**](设置Base平面的亚健康检测参数（SET COMBASEHEALTH）_32217476.md) 命令后等待一个统计周期后才可以使用该命令查询Base平面通信质量。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPODNAME | 源端Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识亚健康检测源端Pod名称，该Pod名称可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| DSTPODNAME | 目的端Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识亚健康检测目的端Pod名称，该Pod名称可以通过使用命令<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMBASEHEALTH]] · Base平面通信质量（COMBASEHEALTH）

## 使用实例

显示Base平面通信质量：

```
%%DSP COMBASEHEALTH: SRCPODNAME="srvcssim-pod-7cdb588b69-22m9f", DSTPODNAME="sfm-pod-5856fd98b4-mgc48";%%
RETCODE = 0  操作成功

结果如下
--------
   源端Pod名称  =  srvcssim-pod-7cdb588b69-22m9f
 目的端Pod名称  =  sfm-pod-5856fd98b4-mgc48
    是否亚健康  =  否
丢包率(千分比)  =  0
错包率(千分比)  =  0
      亚健康值  =  0
平均时延(微秒)  =  463
最大时延(微秒)  =  621
最小时延(微秒)  =  317
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Base平面通信质量（DSP-COMBASEHEALTH）_32217474.md`
