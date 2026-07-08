# 显示Token状态（DSP TOKENSTATUS）

- [命令功能](#ZH-CN_MMLREF_0000001923736544__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001923736544__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001923736544__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001923736544__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001923736544__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001923736544)

**适用NF：SGW-C、PGW-C、AMF、SMF、GGSN、SMSF、NCG**

该命令用于根据实例id查询token状态。

## [注意事项](#ZH-CN_MMLREF_0000001923736544)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001923736544)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001923736544)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务实例的编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该参数来源于通过DSP INSTANCESTATUS查询到的“INSTANCEID”参数。 |

## [使用实例](#ZH-CN_MMLREF_0000001923736544)

怀疑token迁移存在问题时查询。获取指定服务实例下的token状态信息。

```
%%DSP TOKENSTATUS:INSTANCEID="12532461132836508461";%%
RETCODE = 0  操作成功
结果如下
------------------------   
服务实例ID           TOKEN ID           TOKEN状态                                      TOKEN状态持续时间           是否稳态

12532461132836508461  53      smooth_dst        20        TRUE
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001923736544)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 实例ID | 该参数用于表示服务实例的编号。 |
| Token ID | 该参数用于表示token的编号。 |
| Token状态 | 该参数用于表示token的状态。<br>取值说明：<br>- Recovery（Recovery）<br>- Smooth_src（Smooth_src）<br>- Smooth_dst（Smooth_dst）<br>- Recycle（Recycle） |
| 状态持续时间(s) | 该参数用于表示当前token状态持续的时间。 |
| 是否稳态 | Token是否稳态。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
