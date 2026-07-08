# 显示eNodeB邻接关系(DSP ENBNEIBS)

- [命令功能](#ZH-CN_MMLREF_0000001126146258__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146258__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146258__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146258__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146258__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146258__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126146258__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146258)

**适用网元：MME**

查询指定中心eNodeB的邻接eNodeB列表，对系统无影响。

#### [注意事项](#ZH-CN_MMLREF_0000001126146258)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146258)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146258)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146258)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的移动国家码。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的移动网号。<br>取值范围：2～3位数字<br>默认值：无 |
| ENBID | eNodeB 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的标识。<br>取值范围：0～268435455(数值型)<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146258)

查询移动国家码为123，移动网号为03，标识为326的中心eNodeB的邻接eNodeB列表：

DSP ENBNEIBS: ENBTYPE=HOME_ENODEB, MCC="123", MNC="03", ENBID=326;

```
O&M  #61
%%DSP ENBNEIBS: ENBTYPE=HOME_ENODEB, MCC="123", MNC="03", ENBID=326;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
     eNodeB类型    移动国家码    移动网号     eNodeB标识
     Home_eNodeB   123           03           327
     Home_eNodeB   123           03           328
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126146258)

| 输出项名称 | 输出项解释 |
| --- | --- |
| eNodeB类型 | 查询出的邻接eNodeB类型。<br>取值说明:<br>- “HOME_ENODEB”<br>- “MACRO_ENODEB”<br>说明：HOME_ENODEB和MACRO_ENB分别为两种不同的eNodeB类型，该参数是eNodeB的基本信息，在eNodeB侧进行配置。 |
| 移动国家码 | 查询出的邻接eNodeB的移动国家码。 |
| 移动网号 | 查询出的邻接eNodeB的移动网号。 |
| eNodeB标识 | 查询出的邻接eNodeB标识。 |
