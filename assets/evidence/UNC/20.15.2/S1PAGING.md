# 查询S1接口寻呼数据(LST S1PAGING)

- [命令功能](#ZH-CN_MMLREF_0000001172345841__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345841__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345841__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345841__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345841__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345841__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172345841__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345841)

**适用网元：MME**

此命令用于查询eNodeB ID与TAI之间的关联关系。在寻呼用户的过程，MME根据用户所在的TAI查询此表，确定需要下发寻呼消息的eNodeB。

#### [注意事项](#ZH-CN_MMLREF_0000001172345841)

- 此命令执行后立即生效。
- 同时输入参数“移动国家码_移动网号”、“eNodeB类型”和“eNodeB标识”，可查询对应的TAI及所在进程信息。
- 同时输入参数“移动国家码_移动网号”、“eNodeB类型”、“eNodeB标识”和“Tracking Area ID”，参数“Tracking Area ID”将不生效。
- 参数“移动国家码_移动网号”、“eNodeB类型”和“eNodeB标识”必须同时输入或同时不输入。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345841)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345841)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345841)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCCMNC | 移动国家码_移动网号 | 可选必选说明：可选参数<br>参数含义：待查询的eNodeB的移动国家码及移动网号。<br>取值范围：5~6位的字符串，该参数只能由十进制数字组成。<br>默认值：无 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：可选参数<br>参数含义：待查询的eNodeB的类型。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”：28位长的eNodeB。<br>- “MACRO_ENB(MACRO_ENB)”：20位长的eNodeB。<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：可选参数<br>参数含义：待查询的eNodeB ID。<br>取值范围：0~268435455，该参数只能由十进制数字组成。<br>默认值：无 |
| TAI | Tracking Area ID | 可选必选说明：可选参数<br>参数含义：待查询的Tracking Area ID，该参数由MCC、MNC和TAC组成。<br>取值范围：9~10位的字符串，TAC只能由十六进制数字组成。<br>默认值：无 |
| TAIPRESW | 指定TAI前缀查询开关 | 可选必选说明：可选参数<br>参数含义：该参数用于是否开启指定TAI前缀查询S1接口寻呼数据。<br>取值范围：<br>- “OFF(关闭)”：不开启指定TAI前缀查询S1接口寻呼数据。<br>- “ON(开启)”： 开启指定TAI前缀查询S1接口寻呼数据。<br>默认值：“OFF(关闭)”。<br>说明：1、同时输入参数“移动国家码_移动网号”、“eNodeB类型”、“eNodeB标识”或“Tracking Area ID”，参数“指定TAI前缀查询开关”将不生效。<br>2、如果希望按照TAI前缀（如PLMN）查询，可以打开该开关。 |
| TAIPRE | TAI前缀 | 可选必选说明：条件必选参数<br>参数含义：待查询的Tracking Area ID前缀。<br>前提条件：该参数在<br>“指定TAI前缀查询开关”<br>参数配置为<br>“ON(开启)”<br>后生效。<br>取值范围：5~10位的字符串，长度大于PLMN的部分为十六进制数字。<br>默认值：无 |
| S1APLEINDEX | S1AP本端实体标识 | 可选必选说明：可选参数<br>参数含义：待查询S1AP本端实体标识。<br>取值范围：0～63<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务类型名称，可以通过<br>[**LST VNFC**](../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：需要填写LINK或USN对应的名称。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345841)

通过MCCMNC、ENODEBTYPE、ENODEBID查询指定的S1PAGING数据：

LST S1PAGING: MCCMNC="12303",ENODEBTYPE=MACRO_ENB, ENODEBID=69665, SERVICETYPE="USN_VNFC";

```
%%LST S1PAGING: MCCMNC="12303",ENODEBTYPE=MACRO_ENB, ENODEBID=69665
, SERVICETYPE="USN_VNFC";
%%
RETCODE = 0 操作成功。

操作结果如下
-------------------------
                   RU名称 = USN_SP_RU_0065
                   进程号 = 3
      移动国家码_移动网号 = 12303
               eNodeB类型 = MACRO_ENB
               eNodeB标识 = 69665
         Tracking Area ID = 123031102
                  RAT类型 = WB-EUTRAN
NB-IoT Default Paging DRX = 1.28秒
                 服务名称 = USN_VNFC
(结果个数 = 1)

--- END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172345841)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU名称 | 该参数用于指定<br>SPU<br>资源单元名。 |
| 进程号 | 要查询的SGP进程的进程号。 |
| 移动国家码_移动网号 | eNodeB的移动国家码及移动网号，该参数由十进制数字组成。 |
| eNodeB类型 | eNodeB的类型。<br>取值说明:<br>- “HOME_ENB”<br>- “MACRO_ENB” |
| eNodeB标识 | eNodeB ID，该参数由十进制数字组成。 |
| Tracking Area ID | Tracking Area ID，该参数由MCC、MNC和TAC组成，TAC由十六进制数字组成。 |
| RAT类型 | RAT类型<br>取值说明:<br>- “WB-EUTRAN”<br>- “NB-IoT” |
| NB-IoT Default Paging DRX | eNodeB上报给MME的NB-IoT默认寻呼DRX间隔。<br>取值说明:<br>- “1.28秒”<br>- “2.56秒”<br>- “5.12秒”<br>- “10.24秒”<br>- “NULL” |
