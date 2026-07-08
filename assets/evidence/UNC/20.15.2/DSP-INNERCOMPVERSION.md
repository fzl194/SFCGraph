# 显示系统内部部件版本信息（DSP INNERCOMPVERSION）

- [命令功能](#ZH-CN_CONCEPT_0259103441__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259103441__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259103441__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259103441__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259103441__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259103441__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259103441)

该命令用于显示系统内部构件的版本信息。

在日常的维护时，可使用本命令显示系统当前的FENIX版本号、DOPRA版本号、VIST版本号、VPP版本号信息。

#### [注意事项](#ZH-CN_CONCEPT_0259103441)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0259103441)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259103441)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259103441)

显示系统内部版本信息：

```
DSP INNERCOMPVERSION:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
Fenix版本  =  FENIXV100R005C10B090
Dopra版本  =  DOPRA SSP V300R003C00B051
 Vist版本  =  vist_fenix5.0.170421
  Vpp版本  =  VPP V300R003C26SPC217B010
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259103441)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Fenix版本 | 用于表示FENIX版本。 |
| Dopra版本 | 用于表示DOPRA版本。 |
| Vist版本 | 用于表示VIST版本。 |
| Vpp版本 | 用于表示VPP版本。 |
